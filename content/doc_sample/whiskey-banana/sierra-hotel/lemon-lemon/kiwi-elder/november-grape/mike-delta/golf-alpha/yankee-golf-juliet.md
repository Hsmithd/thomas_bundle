# Play: Yankee - setup

- hosts: loadbalancers
  become: false
  vars:
    app_name: "yankee_app"
    retry_count: 4

  tasks:
    - name: Ensure date-task-1 is present
      ansible.builtin.file:
        path: /opt/yankee/date-task-1
        state: directory

    - name: Template date-task-1 config
      ansible.builtin.template:
        src: templates/date-task-1.j2
        dest: /etc/yankee/date-task-1.conf
        mode: '0644'

    # Description:
    # Lorem ipsum dolor sit amet, consectetur adipiscing elit. Excepteur sint occaecat cupidatat non proident, sunt in culpa. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

    - name: Ensure quebec-task-2 is present
      ansible.builtin.file:
        path: /opt/yankee/quebec-task-2
        state: directory

    - name: Template quebec-task-2 config
      ansible.builtin.template:
        src: templates/quebec-task-2.j2
        dest: /etc/yankee/quebec-task-2.conf
        mode: '0644'

    # Description:
    # Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

  handlers:
    - name: restart yankee service
      ansible.builtin.service:
        name: yankee
        state: restarted

## Notes

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

***
Generated: 2025-11-07T18:27:45Z
