# Play: Golf - setup

- hosts: webservers
  become: false
  vars:
    app_name: "golf_app"
    retry_count: 4

  tasks:
    - name: Ensure tango-task-1 is present
      ansible.builtin.file:
        path: /opt/golf/tango-task-1
        state: directory

    - name: Template tango-task-1 config
      ansible.builtin.template:
        src: templates/tango-task-1.j2
        dest: /etc/golf/tango-task-1.conf
        mode: '0644'

    # Description:
    # Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

    - name: Ensure grape-task-2 is present
      ansible.builtin.file:
        path: /opt/golf/grape-task-2
        state: directory

    - name: Template grape-task-2 config
      ansible.builtin.template:
        src: templates/grape-task-2.j2
        dest: /etc/golf/grape-task-2.conf
        mode: '0644'

    # Description:
    # Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. 

    - name: Ensure romeo-task-3 is present
      ansible.builtin.file:
        path: /opt/golf/romeo-task-3
        state: directory

    - name: Template romeo-task-3 config
      ansible.builtin.template:
        src: templates/romeo-task-3.j2
        dest: /etc/golf/romeo-task-3.conf
        mode: '0644'

    # Description:
    # Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

  handlers:
    - name: restart golf service
      ansible.builtin.service:
        name: golf
        state: restarted

## Notes

Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

***
Generated: 2025-11-07T18:27:43Z
