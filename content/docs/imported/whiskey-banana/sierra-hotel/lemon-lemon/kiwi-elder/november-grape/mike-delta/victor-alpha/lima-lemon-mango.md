# Play: Lima - setup

- hosts: db
  become: true
  vars:
    app_name: "lima_app"
    retry_count: 4

  tasks:
    - name: Ensure date-task-1 is present
      ansible.builtin.file:
        path: /opt/lima/date-task-1
        state: directory

    - name: Template date-task-1 config
      ansible.builtin.template:
        src: templates/date-task-1.j2
        dest: /etc/lima/date-task-1.conf
        mode: '0644'

    # Description:
    # Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

    - name: Ensure jasmine-task-2 is present
      ansible.builtin.file:
        path: /opt/lima/jasmine-task-2
        state: directory

    - name: Template jasmine-task-2 config
      ansible.builtin.template:
        src: templates/jasmine-task-2.j2
        dest: /etc/lima/jasmine-task-2.conf
        mode: '0644'

    # Description:
    # Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 

    - name: Ensure banana-task-3 is present
      ansible.builtin.file:
        path: /opt/lima/banana-task-3
        state: directory

    - name: Template banana-task-3 config
      ansible.builtin.template:
        src: templates/banana-task-3.j2
        dest: /etc/lima/banana-task-3.conf
        mode: '0644'

    # Description:
    # Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

  handlers:
    - name: restart lima service
      ansible.builtin.service:
        name: lima
        state: restarted

## Notes

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Excepteur sint occaecat cupidatat non proident, sunt in culpa. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

***
Generated: 2025-11-07T18:27:44Z
