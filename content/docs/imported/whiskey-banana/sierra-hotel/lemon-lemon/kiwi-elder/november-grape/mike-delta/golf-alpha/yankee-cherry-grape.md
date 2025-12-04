# Play: Yankee - setup

- hosts: webservers
  become: false
  vars:
    app_name: "yankee_app"
    retry_count: 1

  tasks:
    - name: Ensure quebec-task-1 is present
      ansible.builtin.file:
        path: /opt/yankee/quebec-task-1
        state: directory

    - name: Template quebec-task-1 config
      ansible.builtin.template:
        src: templates/quebec-task-1.j2
        dest: /etc/yankee/quebec-task-1.conf
        mode: '0644'

    # Description:
    # Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

  handlers:
    - name: restart yankee service
      ansible.builtin.service:
        name: yankee
        state: restarted

## Notes

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Excepteur sint occaecat cupidatat non proident, sunt in culpa. Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

***
Generated: 2025-11-07T18:27:45Z
